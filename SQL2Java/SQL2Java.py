import sys
import os

# Automata's States
initalState = 0
createState = 1
attributeState = 2
constraintState = 3
primaryKeyState = 4
endOfFileState = 5

# Processing variables
actualState = 0
actualFileIndex = 0;
actualLine = ''
actualTable = ''
tables = []
attributesInTable = {}
foreingKeysInTable = {}
primaryKeyInTable = {}


# To treat the SQL Sintax
constraintStatements = ['PRIMARY','INDEX','CONSTRAINT','FOREIGN','REFERENCES','ON']
primaryKeyStatement = 'PRIMARY KEY'
createStatement = 'CREATE TABLE'
openParentesis = '('
closeParentesis = ')'
foreingKeyStatement = 'FOREIGN KEY'
referencesStatement = 'REFERENCES'

# To create the Java class
classHeader = 'public final class'
startOfBlock = '{'
endOfBlock = '}'
endOfLine = ';'
publicStatement = 'public'
classEntryDefinition = 'public static abstract class'
classEntryInterface = 'implements BaseColumns'
entryDefinition = 'public static final String'


def cleanForeingKeyPart(statement):
	fk = statement
	fk = fk.replace(foreingKeyStatement, '')
	fk = fk.replace('`', '')
	fk = fk.replace(openParentesis, '')
	fk = fk.replace(closeParentesis, '')
	fk = fk.lstrip()

	return fk

def cleanReferencesPart(statement):
	ref = statement
	ref = ref.replace('`', '')
	ref = ref.replace(openParentesis, '')
	ref = ref.replace(closeParentesis, '')
	ref = ref.replace(referencesStatement, '')
	ref = ref.lstrip()

	tablePart = ref.split(' ')[0].split('.')[1]
	attrPart = ref.split(' ')[1]

	return tablePart + '.' + attrPart

def getJavaStyle(statement):
	javaStyle = statement
	javaStyle = javaStyle.lower()
	javaStyle = javaStyle.replace('_', ' ')
	javaStyle = javaStyle.title()
	javaStyle = javaStyle.replace(' ', '')
	
	return javaStyle

def isFKFromActualTable(statement, tableName):
	result = False
	statement = statement.replace('`', '')

	theActualTable = '.' + tableName + ' ('
	if theActualTable in statement: 
		result = True

	return result

def nextLineIndex():
	actualFileIndex = actualFileIndex + 1
	return actualFileIndex

def currentLine():
	line = fileByLines[actualFileIndex].upper()
	line = line.replace('`', '')
	
	return line

def cleanPrimaryKeyAttribute(statement):
	primaryKey = statement
	primaryKey = primaryKey.replace('`', '')
	primaryKey = primaryKey.replace(',', '')
	primaryKey = primaryKey.replace(openParentesis, '')
	primaryKey = primaryKey.replace(closeParentesis, '')
	primaryKey = primaryKey.replace(primaryKeyStatement, '')
	primaryKey = primaryKey.lstrip()

	return primaryKey

def cleanTableName(tableName):
	newTableName = tableName
	newTableName = newTableName.replace('`', '')
	newTableName = newTableName.split('.')[1]

	return newTableName

def cleanAttribute(attribute):
	newAttribute = attribute
	newAttribute = newAttribute.replace('`', '')
	newAttribute = newAttribute.replace(',', '')
	newAttribute = newAttribute.lstrip()

	return newAttribute

def isConstraint(statement):
	statements = statement.split(' ')

	for si in statements:
		for constraint in constraintStatements:
			if si == constraint: return True

	return False

def isEndTableDeclaration(statement):
	isEnd = False

	numberOfCloseParentesis = statement.count(closeParentesis)
	numberOfOpenParentesis = statement.count(openParentesis)
	
	if ((numberOfOpenParentesis + 1) - numberOfCloseParentesis) == 0: 
		isEnd = True
	
	return isEnd

def generateDBHelper():
	print 'package hunabsys.classifiertest;'
	print ''
	#print 'import hunabsys.classifiertest.entities'
	print 'import android.content.Context;'
	print 'import android.content.ContentValues;'
	print 'import android.database.sqlite.SQLiteDatabase;'
	print 'import android.database.sqlite.SQLiteOpenHelper;'
	print ''
	print 'public class DatabaseHelper extends SQLiteOpenHelper {'
	print ' '
	print '\t private static final String DATABASE_NAME = "contactsManager";'
	print '\t private static final String LOG = "DatabaseHelper";'
	print '\t private static final int DATABASE_VERSION = 1;'


	# Print each table and its attributes
	print '\t  '
	for table in tables:
		print '\t private static final String TABLE_' + table + ' = "' + table + '";'
		if not attributesInTable.has_key(table): continue

		for attrSQL in attributesInTable[table].split('$'):
			attr = attrSQL.split(' ')[0]
			print '\t private static final String '  + table + '_' + attr + '="' + attr + '";'
			
		tableDef = attributesInTable[table].replace('$', ',') + ' '
		createTableVar = '\t private static final String CREATE_TABLE_' + table + ' = "'
		createTableVar += 'CREATE TABLE ' + table + '( ' + tableDef

		if primaryKeyInTable.has_key(table): 
			createTableVar += ',' + primaryKeyStatement + '(' + primaryKeyInTable[table] + ')'


		if foreingKeysInTable.has_key(table):
			for fkSQL in foreingKeysInTable[table].split('$'):
				fk = fkSQL.split('.')

				createTableVar += ',' + 'FOREIGN KEY (' + fk[0] +') '
				createTableVar += 'REFERENCES ' + fk[1] + '(' + fk[2] + ')'
			
		createTableVar += ')";'

		print createTableVar
		print '\t '



	# prints the constructor and other methodsclear
	print '\t public DatabaseHelper(Context context) {'
	print '\t \tsuper(context, DATABASE_NAME, null, DATABASE_VERSION);'
	print '\t }'
	print '\t '
	print '\t public void closeDB() {'
	print '\t \t SQLiteDatabase db = this.getReadableDatabase();'
	print '\t \t if (db != null && db.isOpen())'
	print '\t \t \tdb.close();'
	print '\t }'
	print '\t '
	print '\t @Override'
	print '\t public void onCreate(SQLiteDatabase db) {'
	for table in tables:
		print '\t \t db.execSQL(CREATE_TABLE_' + table + ');'
	print '\t }'

	print '\t '
	print '\t @Override'
	print '\t public void onUpgrade(SQLiteDatabase db, int oldVersion, int newVersion) {'
	for table in tables:
		print '\t \t db.execSQL("DROP TABLE IF EXISTS " + CREATE_TABLE_' + table +');'

	print '\t \t onCreate(db);'
	print '\t }' 
	print '}' 



def isFinalState(state):
	result = False
	if state == endOfFileState:
		result = True

	return result

def isInitialState(state):
	result = False

	if state == initalState:
		result = True

	return result

def isCreateState(state):
	result = False

	if state == createState:
		result = True

	return result

def isAttributeState(state):
	result = False

	if state == attributeState:
		result = True

	return result

def hasCreateStament(statement):
	result = False

	if createStatement in statement:
		result = True

	return result

def hasConstraint(statement):
	statements = statement.split(' ')

	for si in statements:
		for constraint in constraintStatements:
			if si == constraint: return True

	return False	


def getTableName(statement):
	tableName = statement.replace('`', '')
	tableName = tableName.split('.')[1]

	return tableName




fileName = sys.argv[1]
isValidFile = False


fileByLines = open(fileName).read().split('\n')
numLines = len(fileByLines)


if actualFileIndex == numLines -1 : break

actualState = initalState
while not isFinalState(actualState):
	actualLine = currentLine()

	# Detect the CREATE TABLE Statement
	if isInitialState(actualState):
		if hasCreateStament(actualLine):
			actualState = createState
		else: 
			# Take the next line
			actualFileIndex = actualFileIndex + 1


	# Ignore CREATE TABLE and get the table name
	elif isCreateState(actualState):
		tableName = getTableName(actualLine)
		actualTable = tableName
		tables.append(actualTable)

		# Lets look for the attributes
		actualState = attributeState
		actualFileIndex = actualFileIndex + 1


	# Get the table attributes
	elif isAttributeState(actualState):


		attribute = cleanAttribute(actualLine)
		actualLine = actualLine.replace('`', '')
		actualLine = actualLine.lstrip()

		# If the actual line has any constraint statements
		if isConstraint(actualLine):
			actualState = constraintState
			continue
		
		# It's actually an attribute
		if attributesInTable.has_key(actualTable):
			attributesInTable[actualTable] = attributesInTable[actualTable] + '$' + attribute
		else:
			attributesInTable[actualTable] = attribute

		if isEndTableDeclaration(actualLine):
			actualState = initalState


		actualFileIndex = actualFileIndex + 1



	elif actualState == constraintState:
		if primaryKeyStatement in actualLine:
			actualState = primaryKeyState
			continue
		
		if foreingKeyStatement in actualLine:
			foreingPart = actualLine
			referencesPart = fileByLines[actualFileIndex+1].upper()

			fkStatement = foreingPart + ' ' + referencesPart

			
			# Clean the foreing key
			foreingPart = cleanForeingKeyPart(foreingPart)
			referencesPart = cleanReferencesPart(referencesPart)
			fkStatement = foreingPart + '.' + referencesPart

			actualFileIndex = actualFileIndex + 1
			if foreingKeysInTable.has_key(actualTable):
				foreingKeysInTable[actualTable] = foreingKeysInTable[actualTable] + '$' + fkStatement
			else: 
				foreingKeysInTable[actualTable] = fkStatement


		elif isEndTableDeclaration(actualLine):
			actualState = initalState
			
		actualFileIndex = actualFileIndex + 1


	elif actualState == primaryKeyState:
		primaryKey = cleanPrimaryKeyAttribute(actualLine)

		primaryKeyInTable[actualTable] = primaryKey
		actualState = constraintState

		if isEndTableDeclaration(actualLine):
			actualState = initalState

		actualFileIndex = actualFileIndex + 1


generateDBHelper()


